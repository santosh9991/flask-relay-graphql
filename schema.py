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
class Query(graphene.ObjectType):
    """
    Rootquery
    """
    node = relay.Node.Field()
    Employees = SQLAlchemyConnectionField(EmployeeType)
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
