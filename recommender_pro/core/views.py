from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from google import genai
import joblib
from sklearn.metrics.pairwise import linear_kernel
import numpy as np
import os
from dotenv import load_dotenv
from django.views.decorators.csrf import csrf_exempt

# Load the frozen model into memory ONCE when the server starts
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
tfidf = joblib.load(os.path.join(BASE_DIR, 'core', 'tfidf_vectorizer.pkl'))
train_matrix = joblib.load(os.path.join(BASE_DIR, 'core', 'train_matrix.pkl'))
train_df = joblib.load(os.path.join(BASE_DIR, 'core', 'train_data.pkl'))

load_dotenv()

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

@csrf_exempt
def prototype_home(request):
    recommended_courses = []
    
    if request.method == 'POST':
        user_review = request.POST.get('review_text', '')
        
        if user_review:
            # 1. Convert user input to numbers using our pre-trained vectorizer
            test_vector = tfidf.transform([user_review])
            
            # 2. Calculate similarity instantly
            sim_scores = linear_kernel(test_vector, train_matrix).flatten()
            sorted_idx = np.argsort(sim_scores)[::-1]
            
            # 3. Extract top 10 unique courses
            seen_courses = set()
            for idx in sorted_idx:
                course_name = train_df['Course'].iloc[idx]
                if course_name not in seen_courses:
                    seen_courses.add(course_name)
                    recommended_courses.append(course_name)
                
                if len(recommended_courses) == 10:
                    break
                    
    return render(request, 'home.html', {'recommendations': recommended_courses})


@csrf_exempt
@api_view(['POST'])
def generate_path(request):
    user_input = request.data.get('chat_message', '')
    print(f"\n--- 1. Received user goal: '{user_input}' ---")
    
    # 1. Get ALL the closest courses (Sorted highest to lowest)
    test_vector = tfidf.transform([user_input])
    sim_scores = linear_kernel(test_vector, train_matrix).flatten()
    all_indices = np.argsort(sim_scores)[::-1] 
    
    # 2. Extract and DEDUPLICATE to ensure the AI gets distinct courses
    unique_courses = []
    seen = set()
    for idx in all_indices:
        course = train_df['Course'].iloc[idx]
        if course not in seen:
            seen.add(course)
            unique_courses.append(course)
        # Stop once we have exactly 7 distinct courses to build a path
        if len(unique_courses) == 10: 
            break
            
    print(f"--- 2. TF-IDF matched unique courses: {unique_courses}. Sending to Gemini... ---")
    
    # 3. Use the strict prompt to force distinct milestones
    prompt = f"""
    A learner wants to achieve this goal: "{user_input}"
    Here are the top unique courses recommended for them: {unique_courses}
    
    Act as an AI Learning Assistant. Create a structured learning roadmap.
    CRITICAL RULE: You MUST create a milestone for EVERY SINGLE course in the list above. Do not skip any courses. Do not combine them into one step.
    
    For each course, provide:
    1. Milestone Order (1, 2, 3...)
    2. A 1-sentence explanation of WHY this specific course helps them achieve their goal.
    
    Format strictly as a JSON object with a "learning_path" array containing objects with "course_name", "milestone", and "explanation" keys.
    """
    
    try:
        response = client.models.generate_content(
            model='gemini-3.6-flash',
            contents=prompt,
        )
        print("--- 3. Gemini finished generating! Sending to Angular. ---")
        return Response({"ai_response": response.text})
        
    except Exception as e:
        print(f"--- ERROR: {str(e)} ---")
        return Response({"error": str(e)}, status=500)