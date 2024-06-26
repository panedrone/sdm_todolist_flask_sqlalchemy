A project demonstrating how to use [SQL DAL Maker](https://github.com/panedrone/sqldalmaker) + Python/Flask-SQLAlchemy.

Front-end is written in Vue.js 2.7. RDBMS is SQLite3.

![sdm-todo-app.png](sdm-todo-app.png)

sdm.xml

```xml

<sdm>
    
    <dto-class name="sa-Project" ref="projects"/>

    <dto-class name="sa-ProjectLi" ref="get_projects.sql"/>

    <dto-class name="sa-Task" ref="tasks"/>

    <dto-class name="sa-TaskLi" ref="tasks">
        <header><![CDATA[    """
    Task list item
    """
    __table_args__ = {'extend_existing': True}]]></header>
        <field column="t_comments" type="-"/>
    </dto-class>

    <dao-class name="_ProjectsDao">
        <crud dto="sa-Project"/>
    </dao-class>

    <dao-class name="_TasksDao">
        <crud dto="sa-Task"/>
    </dao-class>

</sdm>
```

Generated code in action:

```python
from dbal.data_store import scoped_ds
from dbal.project import Project
from dbal.projects_dao_ex import ProjectsDao
from dbal.task import Task


def get_all_projects():
    ds = scoped_ds()
    return ProjectsDao(ds).get_all_projects()


def read_project(p_id):
    ds = scoped_ds()
    project = ProjectsDao(ds).read_project(p_id)
    return project


def create_project(p_name):
    ds = scoped_ds()
    project = Project(p_name=p_name)
    ProjectsDao(ds).create_project(project)
    ds.commit()


def update_project(p_id, p_name):
    ds = scoped_ds()
    ProjectsDao(ds).rename(p_id, p_name)
    ds.commit()


def delete_project(p_id):
    ds = scoped_ds()
    ds.delete_by_filter(Task, {"p_id": p_id})
    ProjectsDao(ds).delete_project(p_id)
    ds.commit()

```
