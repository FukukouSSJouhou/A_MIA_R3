const pynode = require('@fukukoussjouhou/pynode')

if (process.platform === 'linux') {
    pynode.dlOpen('libpython3.10.so')
}

// add current path as Python module search path, so it finds our test.py
pynode.startInterpreter()
pynode.appendSysPath('./')
pynode.appendSysPath('./venv/Lib/site-packages')
loggerobj = (strkun) => {
    console.log(strkun);
}
const pyclasstest1 = pynode.pyimport('A_MIA_R3_Core.nodewrap.A_MIR_R3_nodev2');
classi = pyclasstest1.get("A_MIR_R3_node2").call(loggerobj);
classi.get("setFilename").call("./koizumi_7_30.mp4");
classi.get("run").call();
classi.get("create_syoriobj").call();
console.log(classi.get("getNextImageBase64").call());