import balanced

balanced.configure('ak-test-14W5azoiV99O1XiPwZ3faH10MaUdZ1kCA')

debit = balanced.Debit.find('/v1/marketplaces/TEST-MP52IlCmywk6hGbgS75QSlN/debits/WD2lQO6cFyxyTWj6mLQ6zFDO')
debit.description = 'New description for debit'
debit.meta = {
  'facebook.id': '1234567890',
  'anykey': 'valuegoeshere',
}
debit.save()