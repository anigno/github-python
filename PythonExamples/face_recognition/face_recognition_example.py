import face_recognition

# Load the image
image = face_recognition.load_image_file("image.jpg")

# Detect faces in the image
face_locations = face_recognition.face_locations(image)

# Identify the faces in the image
face_encodings = face_recognition.face_encodings(image, face_locations)

# Get the names of the known people
known_face_names = ["John Doe", "Jane Doe"]

# Identify the faces in the image
for face_encoding in face_encodings:
    # Try to match the face encoding to a known person
    matches = face_recognition.compare_faces(known_face_names, face_encoding)

    # If there is a match, print the name of the known person
    if True in matches:
        print(known_face_names[matches.index(True)])

    # Otherwise, print "Unknown person"
    else:
        print("Unknown person")