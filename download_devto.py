import requests
import json
import os
from pathlib import Path

def download_posts(api_key, username, output_dir='posts'):
    """
    Download all blog posts from dev.to for a specific user
    
    Args:
        api_key (str): Your dev.to API key
        username (str): Your dev.to username
        output_dir (str): Directory to save posts (default: 'posts')
    """
    base_url = 'https://dev.to/api/articles/me'
    headers = {'api-key': api_key}
    page = 1
    all_posts = []
    
    # Create output directory if it doesn't exist
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    while True:
        response = requests.get(
            f'{base_url}?page={page}',
            headers=headers
        )
        
        if response.status_code != 200:
            print(f'Error fetching posts: {response.status_code}')
            break
            
        posts = response.json()
        if not posts:
            break
            
        all_posts.extend(posts)
        page += 1
    
    print(f'Found {len(all_posts)} posts')
    
    # Save each post
    for post in all_posts:
        filename = f"{post['published_at'][:10]}_{post['slug']}.md"
        filepath = os.path.join(output_dir, filename)
        
        # Get full article content
        article = requests.get(
            f"https://dev.to/api/articles/{post['id']}",
            headers=headers
        ).json()
        
        # Save post content
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"---\n")
            f.write(f"title: {post['title']}\n")
            f.write(f"published: {post['published_at']}\n")
            f.write(f"tags: {','.join(post['tags'])}\n")
            f.write(f"canonical_url: {post['canonical_url']}\n")
            f.write(f"---\n\n")
            f.write(article['body_markdown'])
            
        print(f'Saved: {filename}')

if __name__ == '__main__':
    api_key = input('Enter your dev.to API key: ')
    username = input('Enter your dev.to username: ')
    download_posts(api_key, username)