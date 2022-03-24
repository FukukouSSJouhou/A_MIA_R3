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
    let image_list: Array<string> = [
        "https://via.placeholder.com/300x300",
        
        "https://via.placeholder.com/300x300",
        
        "https://via.placeholder.com/300x300",
        
        "https://via.placeholder.com/300x300",
        
        "https://via.placeholder.com/300x300"
    ]
    const [openSnackbar, setOpenSnackbar] = React.useState(false);
    const [selectedIndex,setselectedIndex]=React.useState(0);

    const clicked_btkun=(index:number)=>{
        setselectedIndex(index);
        setOpenSnackbar(true);
    }
    const handleClose=(event?:React.SyntheticEvent|Event,reason?:string)=>{
        if(reason==="clickaway"){
            return;
        }
        setOpenSnackbar(false);
    }
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
}