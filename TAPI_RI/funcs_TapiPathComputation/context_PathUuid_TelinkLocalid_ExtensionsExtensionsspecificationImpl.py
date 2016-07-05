import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_PathUuid_TelinkLocalid_ExtensionsExtensionsspecificationImpl:

    @classmethod
    def get(cls, uuid, localId, extensionsSpecification):
        print 'handling get'
        if uuid in be.Context._path:
            if localId in be.Context._path[uuid]._telink:
                if extensionsSpecification in be.Context._path[uuid]._telink[localId]._extensions:
                    return be.Context._path[uuid]._telink[localId]._extensions[extensionsSpecification]
                else:
                    raise KeyError('extensionsSpecification')
            else:
                raise KeyError('localId')
        else:
            raise KeyError('uuid')
