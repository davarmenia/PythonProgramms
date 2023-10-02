import requests
import json

def formulaOneBet(year, round, userBets):
    response = json.loads(requests.get('http://ergast.com/api/f1/{}/{}/driverStandings.json'.format(year, round)).text)
    bets = dict()
    bets_per_user = [0] * len(userBets)
    successful_bets_per_user = [0] * len(userBets)

    for i, b in enumerate(userBets):
        for driverId, position, amount in b:
            amount = int(amount)
            bets_per_user[i] += amount
            bets.setdefault((driverId, position), []).append((i, amount))

    for p in response['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']:
        for userId, amount in bets.get((p['Driver']['driverId'], p['positionText']), []):
            successful_bets_per_user[userId] += amount

    betsPerUser = sum(bets_per_user)
    SucBetsPerUser = sum(successful_bets_per_user)

    if SucBetsPerUser == 0:
        return -max(bets_per_user)
    return max(a * betsPerUser / SucBetsPerUser - b for a, b in zip(successful_bets_per_user, bets_per_user))

year = 2008
round = 5
userBets = [[["massa", "2", "200"]], [["webber", "7", "100"]]]
print(formulaOneBet(year,round,userBets))
'''
year = 2008
round = 5
userBets = [[["massa", "2", "200"], ["webber", "7", "100"], ["alonso", "1", "100"]], [["massa", "1", "200"]]]

**************
year = 2017
round = 1
userBets = [[["michael_schumacher","6","500"]]] 

***************
year = 1978
round = 1
userBets = [[["reutemann","7","20"]],  [["peterson","5","140"]],  [["hunt","5","160"]]]

'''
