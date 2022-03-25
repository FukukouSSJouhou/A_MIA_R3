import { Button, Grid, Paper, Snackbar } from '@mui/material';
import MuiAlert, { AlertProps } from '@mui/material/Alert';
import * as React from 'react';
const Alert = React.forwardRef<HTMLDivElement, AlertProps>(function Alert(
    props,
    ref,
  ) {
    return <MuiAlert elevation={6} ref={ref} variant="filled" {...props} />;
  });
export default function ImageSelectPage(): React.ReactElement {
    let ws=React.useRef<WebSocket>(null!);
    React.useEffect(()=>{
        ws.current=new WebSocket('ws://localhost:5001');
        ws.current.onmessage=(e)=>{
            console.log(e.data);
        }
        return ()=>{
            ws.current.close();
        }
    },[]);
    /*let image_list: Array<string> = [
        "https://via.placeholder.com/300x300",
        
        "https://via.placeholder.com/300x300",
        
        "https://via.placeholder.com/300x300",
        
        "https://via.placeholder.com/300x300",
        
        "https://via.placeholder.com/300x300"
    ]*/
    const [image_list,setImageList]=React.useState<Array<string>>([]);
    const [openSnackbar, setOpenSnackbar] = React.useState(false);
    const [selectedIndex,setselectedIndex]=React.useState(0);
    const [canselect,setcanselect]=React.useState(false);

    React.useEffect(()=>{
        if(!ws.current) return;
        ws.current.onmessage=e=>{
            const message = JSON.parse(e.data);
            //console.log("e", message.data);
            setImageList(message.data);
            setcanselect(true);
        }
    },[]);
    const clicked_btkun=(index:number)=>{
        let sendobject={
            command:"selectedimg",
            indexid:index
        };
        setselectedIndex(index);
        setOpenSnackbar(true);
        ws.current.send(JSON.stringify(sendobject));
    }
    const handleClose=(event?:React.SyntheticEvent|Event,reason?:string)=>{
        if(reason==="clickaway"){
            return;
        }
        setOpenSnackbar(false);
    }
    if(canselect){

        return (
            <>
                <Grid container rowSpacing={1} columnSpacing={{ xs: 2, sm: 2, md: 3 }}>
                    {image_list.map((image_url: string, index: number) => {
                        return (
                            <Grid item xs={3}>
                                <Button onClick={()=>{clicked_btkun(index)}}>
                                    <Paper elevation={3} >
                                        <img src={image_url} alt="" />
                                    </Paper></Button>
                            </Grid>
                        );
                    }
                    )}
                </Grid>
          <Snackbar open={openSnackbar} autoHideDuration={6000} onClose={handleClose}>
            <Alert onClose={handleClose} severity="success" sx={{ width: '100%' }}>
              Selected {selectedIndex}!
            </Alert>
          </Snackbar>
            </>
        );
    }else{
        return (
            <>
            Waiting...
            </>
        );
    }
}