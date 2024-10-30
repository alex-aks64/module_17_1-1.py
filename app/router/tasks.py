from fastapi import APIRouter

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("/")
def all_tasks(): pass


@router.get("/task_id")
def get_task(): pass


@router.post("/create")
def create_task(): pass


@router.put("/update")
def update_task(): pass


@router.delete("/delete")
def delete_task(): pass