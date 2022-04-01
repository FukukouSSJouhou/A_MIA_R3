const pynode = require('@fridgerator/pynode')



// add current path as Python module search path, so it finds our test.py
pynode.appendSysPath('./')
pynode.appendSysPath('./venv/Lib/site-packages')

// open the python file (module)
pynode.openFile('pynodetestmod')

// call the python function and get a return value
pynode.call('tintin', 9, 2, (err, result) => {
  if (err) return console.log('error : ', err)
  console.log(result);
})