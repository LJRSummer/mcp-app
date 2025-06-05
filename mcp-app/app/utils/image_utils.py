def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg'}

def get_image_hash(image_path):
    with Image.open(image_path) as img:
        return imagehash.phash(img)

def calc_similarity_score(hash1, hash2, hash_size=64):
    distance = abs(hash1 - hash2)
    return 1 - distance / hash_size

def group_similarity_score(image_folder):
    image_files = [f for f in os.listdir(image_folder) if allowed_file(f)]
    hashes = [get_image_hash(os.path.join(image_folder, f)) for f in image_files]
    scores = []
    max_pair = (None, None)
    max_score = -1
    for i, hash1 in enumerate(hashes):
        for j in range(i + 1, len(hashes)):
            hash2 = hashes[j]
            score = calc_similarity_score(hash1, hash2)
            scores.append(score)
            if score > max_score:
                max_score = score
                max_pair = (image_files[i], image_files[j])
    if not scores:
        return 0, 0, 0, (None, None)
    avg_score = sum(scores) / len(scores)
    min_score = min(scores)
    return avg_score, max_score, min_score, max_pair