import Epate

class UListError(Exception):

    def __init__(self, message):
        self.message = message


class CSRunningError(Exception):

    def __init__(self, message):
        self.message = message

ul = None

def setUList(ulist):
    if ul is None:
        ul = ulist
    else:
        raise UListError(
            'UList is seted,use setUList() to set it.')


def delUList():
    if ul is not None:
        ul = None
    else:
        raise UListError(
            'UList is not seted,use setUList() to set it.'
        )


def like(workid, times):
    if ul is not None:
        for i in range(times):
            Epate.login(ul[i]['un'], ul[i]['pw'])
            doing = Epate.like(workid)
            if doing != '200':
                raise CSRunningError(
                    f'failure of the {i+1} operation,HTTPCode is {doing}.')
            Epate.logout()
    else:
        raise UListError(
            'UList is not seted,use setUList() to set it.'
        )


def coll(workid, times):
    if ul is not None:
        for i in range(times):
            Epate.login(ul[i]['un'], ul[i]['pw'])
            doing = Epate.coll(workid)
            if doing != '200':
                raise CSRunningError(
                    f'failure of the {i+1} operation,HTTPCode is {doing}.')
            Epate.logout()
    else:
        raise UListError(
            'UList is not seted,use setUList() to set it.'
        )


def fork(workid, times):
    if ul is not None:
        for i in range(times):
            Epate.login(ul[i]['un'], ul[i]['pw'])
            doing = Epate.fork(workid)
            if doing != '200':
                raise CSRunningError(
                    f'failure of the {i+1} operation,HTTPCode is {doing}.')
            Epate.logout()
    else:
        raise UListError(
            'UList is not seted,use setUList() to set it.'
        )