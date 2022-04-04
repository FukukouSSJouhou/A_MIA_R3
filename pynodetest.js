const pynode = require('@fukukoussjouhou/pynode')


// add current path as Python module search path, so it finds our test.py
pynode.startInterpreter()
pynode.appendSysPath('./')
pynode.appendSysPath('./venv/Lib/site-packages')
const pyclasstest1 = pynode.pyimport('pynodetestmod');
classi=pyclasstest1.get("pyclasstest").call('4','3');
result=classi.get("run").call((a,b,c)=>{
  console.log(arguments);
  return b*c;
})
console.log(result);