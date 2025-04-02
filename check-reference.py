#!/usr/bin/env python3
import re
import os
import sys
import json

def check_references():
    print("Verifying Unit 3 References...")
    
    # Read the index.html file
    try:
        with open('index.html', 'r', encoding='utf-8') as file:
            content = file.read()
    except Exception as e:
        print(f"Error reading index.html: {e}")
        return False
    
    # Check for title
    title_pattern = r'<title>([^<]+)</title>'
    title_match = re.search(title_pattern, content)
    if title_match:
        title = title_match.group(1)
        if "Unit 3" not in title:
            print(f"❌ Title does not reference Unit 3: {title}")
            return False
        else:
            print(f"✅ Title references Unit 3: {title}")
    
    # Check for exam weight percentage
    exam_weight_pattern = r'Unit 3 represents (\d+-\d+)% of the AP Statistics Exam'
    exam_weight_match = re.search(exam_weight_pattern, content)
    if exam_weight_match:
        exam_weight = exam_weight_match.group(1)
        if exam_weight != "12-15":
            print(f"❌ Incorrect exam weight: {exam_weight}%")
            return False
        else:
            print(f"✅ Correct exam weight: {exam_weight}%")
    else:
        print("❌ Could not find exam weight percentage")
        return False
    
    # Check PDF file paths
    pdf_path_pattern = r'"pdfs/unit(\d+)/.*\.pdf"'
    pdf_paths = re.findall(pdf_path_pattern, content)
    incorrect_paths = [path for path in pdf_paths if path != "3"]
    
    if incorrect_paths:
        print(f"❌ Found {len(incorrect_paths)} PDF paths that don't reference Unit 3")
        return False
    else:
        print(f"✅ All PDF paths reference Unit 3 ({len(pdf_paths)} paths checked)")
    
    # Check topic IDs in pdfFiles array
    topic_id_pattern = r'id:\s*"(\d+)-'
    topic_ids = re.findall(topic_id_pattern, content)
    incorrect_ids = [topic_id for topic_id in topic_ids if topic_id != "3"]
    
    if incorrect_ids:
        print(f"❌ Found {len(incorrect_ids)} topic IDs that don't reference Unit 3")
        return False
    else:
        print(f"✅ All topic IDs reference Unit 3 ({len(topic_ids)} IDs checked)")
    
    # Check video URLs
    video_url_pattern = r'videoUrl:\s*"https://apclassroom\.collegeboard\.org/[^"]+sui=33,(\d+)"'
    video_urls = re.findall(video_url_pattern, content)
    incorrect_urls = [url for url in video_urls if url != "3"]
    
    if incorrect_urls:
        print(f"❌ Found {len(incorrect_urls)} video URLs that don't reference Unit 3")
        return False
    else:
        print(f"✅ All video URLs reference Unit 3 ({len(video_urls)} URLs checked)")
    
    print("✅ All checks passed! The index.html file is correctly referencing Unit 3.")
    return True

if __name__ == "__main__":
    success = check_references()
    sys.exit(0 if success else 1)