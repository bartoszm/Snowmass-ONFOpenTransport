import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_PathcompserviceUuid_Routingconstraint_ExcludepathLocalidImpl:

    @classmethod
    def get(cls, uuid, localId):
        print 'handling get'
        if uuid in be.Context._pathCompService:
            if localId in be.Context._pathCompService[uuid]._routingConstraint._excludePath:
                return be.Context._pathCompService[uuid]._routingConstraint._excludePath[localId]
            else:
                raise KeyError('localId')
        else:
            raise KeyError('uuid')
