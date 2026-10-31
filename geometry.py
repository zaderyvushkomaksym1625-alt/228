def calculate_rectangle(width, height):
    if width <= 0 or height <= 0:
        return None
    
    area = width * height
    perimeter = (width * height) * 2  # Навмисна помилка у формулі периметра
    
    return {"area": area, "perimeter": perimeter}