
def create_task(title, description):
    if not title:
        raise ValueError("Title is required")
    return {"title": title, "description": description}