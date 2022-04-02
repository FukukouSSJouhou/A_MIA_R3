import pynode from '@fukukoussjouhou/pynode';
class A_MIA_R3_PythonWraps{
    pyinstance:any;
    constructor(){
        this.pyinstance=pynode.pyimport("A_MIA_R3_Core.nodewrap.A_MIR_R3_node")
    }
}
export default A_MIA_R3_PythonWraps;