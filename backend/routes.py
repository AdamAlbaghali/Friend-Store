from app import app, db
from flask import request, jsonify
from models import Friend

# Get all friends
@app.route("/api/friends", methods=["GET"])
def get_friends():
    friends = Friend.query.all()
    print(f"Number of friends fetched: {len(friends)}")  # Debugging print
    result = [friend.to_json() for friend in friends]
    print(f"Friends data: {result}")  # Debugging print
    return jsonify(result)

# Create a friend
@app.route("/api/friends", methods=["POST"])
def create_friend():
    try:
        data = request.json

        name = data.get("name")
        role = data.get("role")
        description = data.get("description")
        gender = data.get("gender")

        #fetch avatar image based on gender
        if gender == "male":
            img_url = f"https://avatar.iran.liara.run/public/boy?username={name}"
        elif gender == "female":
            img_url = f"https://avatar.iran.liara.run/public/girl?username={name}"
        else:
            img_url = None

        new_friend = Friend(name=name, role=role, description=description, gender=gender,
                        img_url=img_url)
    
        db.session.add(new_friend)
         ## need to commit this ^

        db.session.commit()

        return jsonify({"msg":"Friend created successfully"}),201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error":str(e)}), 500
