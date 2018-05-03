import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import *

class EmployeeType(SQLAlchemyObjectType):
    """Creates a SQLAlchemyObjectType for model CPUModel
    """
    class Meta:
        model = EmployeeModel
        interfaces = (relay.Node,)

class DepartmentType(SQLAlchemyObjectType):
    """Creates a SQLAlchemyObjectType for model CPUModel
    """
    class Meta:
        model = DepartmentModel
        interfaces = (relay.Node,)
    Employees = SQLAlchemyConnectionField(EmployeeType,
        department_id=graphene.String())
    def resolve_Employees(self,info,
        department_id=DepartmentModel.department_id):
        query = EmployeeType.get_query(info)
        print(department_id)
        if department_id:
            return query.filter(
            EmployeeModel.department_id==department_id)
class Query(graphene.ObjectType):
    """
    Rootquery
    """
    # node = relay.Node.Field()
    Employees = SQLAlchemyConnectionField(EmployeeType,
    departmentId = graphene.List(graphene.Int))
    def resolve_Employees(self,info,departmentId=None):
        query = EmployeeType.get_query(info)
        if departmentId:
            return query.filter(
            EmployeeModel.department_id.in_(departmentId))
        return query.all()
    Departments = SQLAlchemyConnectionField(DepartmentType)
    # all_mots_appl = SQLAlchemyConnectionField(MOTSAppl)
    # mots_appl = graphene.List(lambda: MOTSAppl,
    #                         status=graphene.String())
    # # all_mots_appl = graphene.List(MOTSAppl, q=graphene.String())
    # def resolve_mots_appl(self, info,status=None):#location_id=None):
    #     # status = args.get('status')
    #     query = MOTSAppl.get_query(info)
    #     return query.filter(MOTSApplModel.status==status).all()#limit(1)
schema = graphene.Schema(query=Query)
