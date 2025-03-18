from pymongo import MongoClient

# Connect to MongoDB (default localhost:27017)
client = MongoClient("mongodb://localhost:27017/")

# Create or connect to 'blogDB'
db = client["blogDB"]

# Create or connect to 'posts' collection
posts_collection = db["posts"]

# Sample blog post
blog_post = {
    "title": "My First Blog Post",
    "author": "Sukhdeep Singh",
    "content": "This is a sample blog post stored in MongoDB using PyMongo.",
    "tags": ["Python", "MongoDB", "PyMongo"],
    "date": "2025-03-18"
}

# Insert the blog post
post_id = posts_collection.insert_one(blog_post).inserted_id
print(f"Blog post inserted with ID: {post_id}")

# Retrieve and display all blog posts
print("\nAll Blog Posts:")
for post in posts_collection.find():
    print(f"Title: {post['title']}, Author: {post['author']}, Content: {post['content']}")
