
class TestData:
    #login page:
    userName = "itay1709"
    email = "itay.zisman@payboxapp.com"
    password = "1234"
    loginCode = "123"

    #hompe page:
    expectedUpperNavigator = ["LOG", "ADMINS", "CONF EDITOR", "CS", "BI", "MASAV", "SCRIPTS", "SMP", "FRAUD", "EXTRACT DATA", "MARKETING", "DB EDITOR", "LOGOUT"]
    expectedEntityNavigator = ["User", "Group", "Transaction", "POF User", "Card", "P2P Gr", "Logs"]
    expectedUserSubMenu = ['phone', 'email', 'name', 'pid', 'israeli id', 'uuid', 'Bank Acc', 'parmx', '4-digits', 'group name', 'groupId']
    expectedGroupSubMenu = ['Recent', 'title', 'Member.Phone', 'Manager.Phone', 'Group Id', 'min balance', 'M.uId', 'M.Email', 'M.Name']
    expectedTransactionSubMenu = ['recent', 'Rejected (rec)', 'Type', 'U. Id', 'parmx', 'trans Id', 'group Id', 'ex. trans Id', 'ex. card num']
    expectedPofSubMenu = ['phone', 'email', 'name', 'id', 'idNumber']
    expectedCardSubMenu = ['israeli id', 'token', 'user Id', 'user phone', '4-digits']
    userDetails1 = ['איתי זיסמן בדיקות הכי טוב', '972-502142090', 'test@test123.com', '5ede04bbb96fa3000a67ae7e']
    userDetails2 = ['איתי בדיקות 2', '972-502142080', 'itayzis@gmail.com', '5f3b63194c900f000a40122f']
    groupDetails1 = ['כולם משלמים', '972-502142090', 'איתי זיסמן בדיקות הכי טוב', '210.08', '349.92', '560', '28/02/2021', '11', '603bb03b7b3fd0000a6c3168']

    #user page:
    expectedBasicActionsMenu = ['Set New Phone Number', 'Delete user', 'Set New Pin', 'Set Pin Status', 'Set Security Answer', 'Change Sec Question', '', '', 'Set A New Email', 'Set Profile Type', 'Delete user’s ID number', 'Change user’s ID number', 'Export user’s history']
    expectedMoreActionsMenu = ['Change KYC level  New', 'Add new KYC document  New', 'Watch List ', 'Remove from Watch List ', 'Block ', 'Un-Block ', 'Ban ', 'Ukraine Release  New', 'Un-Ban ', '', '', 'Manual Bank Withdraw ', '', '', 'Claim Money ', 'Rollback Money  New', 'Unset Unique Withdraw BANK fees ', 'Depracted Actions \nAdd Unique Pay Fees \nAdd Unique Withdraw BANK Fees \nUnset Unique Pay fees \nUnset Unique Withdraw CARD fees \nAdd Unique Withdraw CARD Fees ']
    expectedProfileTypeList = ["", "Personal", "Business - Exempt", "Business - Licensed", "Business - Corporate", "Non - Profit Organization", "Governmental", "Business - Unclassified"]