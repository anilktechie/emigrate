#

import apipkg
apipkg.initpkg(__name__, {
    'actions': {
        'ActionCreate': 'emigrate._actions._ActionCreate:ActionCreate',
        'ActionStatus': 'emigrate._actions._ActionStatus:ActionStatus',
        'ActionList'  : 'emigrate._actions._ActionList:ActionList',
        'ActionHelp'  : 'emigrate._actions._ActionHelp:ActionHelp',
        'ActionUp'    : 'emigrate._actions._ActionUp:ActionUp',
        'ActionDown'  : 'emigrate._actions._ActionDown:ActionDown',
        'ActionRedo'  : 'emigrate._actions._ActionRedo:ActionRedo',
        'ActionInfo'  : 'emigrate._actions._ActionInfo:ActionInfo',
        'ActionConfig': 'emigrate._actions._ActionConfig:ActionConfig',
    },
    'mysql': {
        'MySQLClient'      : 'emigrate._mysql._MySQLClient:MySQLClient',
        'MySQLTransaction' : 'emigrate._mysql._MySQLTransaction:MySQLTransaction',
    },
    'BaseAction'      : "emigrate._BaseAction:BaseAction",
    'Application'     : "emigrate._Application:Application",
    'Migration'       : "emigrate._Migration:Migration",
    'OptionsReader'   : "emigrate._OptionsReader:OptionsReader",
    'MigrationLoader' : "emigrate._MigrationLoader:MigrationLoader",
    'MigrationActor'  : "emigrate._MigrationActor:MigrationActor",
})
