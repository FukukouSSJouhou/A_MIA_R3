import { Alert, Box, Button, Dialog, DialogActions, DialogContent, DialogContentText, DialogTitle, Grid, Paper, Snackbar, Step, StepLabel, Stepper, Typography } from '@mui/material';
import React, * as react from 'react';

const steps = ['Select File Name', 'Select target face', 'Wait for generating img..'];
export default function IndexPage(): React.ReactElement {
  const [vfilename, setvfilename] = React.useState<string>(null!);
  const [activeStep, setActiveStep] = React.useState(0);
  const [skipped, setSkipped] = React.useState(new Set<number>());
  const [allimageselected,setAllimageselected]=React.useState(false);
  const [filenotfoundialogopen,setfilenotfoundialogopen]=React.useState(false);
  
  const [image_list,setImageList]=React.useState<Array<string>>([]);
  const [canselect,setcanselect]=React.useState(false);
  const [openSnackbar, setOpenSnackbar] = React.useState(false);
  const [selectedIndex,setselectedIndex]=React.useState(0);
  const handlefilenotfoundialogopen=()=>{
    setfilenotfoundialogopen(true);
  }
  const callbacksetimagekun=(datakun:string)=>{
    const message = JSON.parse(datakun);
    setImageList(message.data);
  }
  const handlefilenotfoundialogclose=()=>{
    setfilenotfoundialogopen(false);
  }
  const isStepOptional = (step: number) => {
    return step === 1;
  };

  const isStepSkipped = (step: number) => {
    return skipped.has(step);
  };
  
  window.mia_electron_api.Setimagelistsendcallback(callbacksetimagekun);
  const clicked_btkun=(index:number)=>{
    setselectedIndex(index);
    setOpenSnackbar(true);
    window.mia_electron_api.setselectimg(index)
    setcanselect(false);
}
const handleClose=(event?:React.SyntheticEvent|Event,reason?:string)=>{
    if(reason==="clickaway"){
        return;
    }
    setOpenSnackbar(false);
}
  const button_clicked = () => {
    //console.log("clicked");
    window.mia_electron_api.openVideoFileDialog("Open File").then(
      (pathobj) => {
        if (pathobj.status === true) {
          setvfilename(pathobj.path);
        } else {
          //setvfilename("");
          //no work!
        }
      });
  };
  const handleNext = () => {
    //次へボタンが押されたときの処理
    switch (activeStep) {
      case 0:
        console.log("Zero");
        //ファイルの存在チェック
        window.mia_electron_api.fileExistsAsync(vfilename)
          .then((result) => {
            //チェック完了後に呼び出される
            if (result) {
              //存在するなら
              window.mia_electron_api.set_filename(vfilename).then((resultkun334)=>{
                console.log(resultkun334);
                let newSkipped = skipped;
                if (isStepSkipped(activeStep)) {
                  newSkipped = new Set(newSkipped.values());
                  newSkipped.delete(activeStep);
                }
  
                setActiveStep((prevActiveStep) => prevActiveStep + 1);
                setSkipped(newSkipped);
                window.mia_electron_api.run();
              });
            } else {
              //しないなら
              console.log("You can't");
              setfilenotfoundialogopen(true);
            }
          }
          );
        return;
      case 1:
          if(!allimageselected){
            return;
          }
    }
    console.log(activeStep);
    let newSkipped = skipped;
    if (isStepSkipped(activeStep)) {
      newSkipped = new Set(newSkipped.values());
      newSkipped.delete(activeStep);
    }

    setActiveStep((prevActiveStep) => prevActiveStep + 1);
    setSkipped(newSkipped);
  };

  const handleBack = () => {
    setActiveStep((prevActiveStep) => prevActiveStep - 1);
  };
  /*
    const handleSkip = () => {
      if (!isStepOptional(activeStep)) {
        // You probably want to guard against something like this,
        // it should never occur unless someone's actively trying to break something.
        throw new Error("You can't skip a step that isn't optional.");
      }
  
      setActiveStep((prevActiveStep) => prevActiveStep + 1);
      setSkipped((prevSkipped) => {
        const newSkipped = new Set(prevSkipped.values());
        newSkipped.add(activeStep);
        return newSkipped;
      });
    };
  */
  const handleReset = () => {
    setActiveStep(0);
  };
  const SecondPage=()=>{
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
    <Snackbar open={openSnackbar} autoHideDuration={6000} onClose={handleClose}>
      <Alert onClose={handleClose} severity="success" sx={{ width: '100%' }}>
        Selected {selectedIndex}!
      </Alert>
    </Snackbar>
      </>
    ); 
    }
  }
  const naibuyouso = () => {
    switch (activeStep) {
      case 0:
        return (
          <>

            {vfilename}
            <br />
            <Button onClick={button_clicked}>
              Select video file
            </Button>
            <br />
          </>
        );
      case 1:
        return (<SecondPage />);
      default:
        return "Default!";
    }
  }
  const DialogAlertkun=(openkun:boolean,handleClose:any,filenamekun:string)=>{
    return(
      
    <div>
    <Dialog
      open={openkun}
      onClose={handleClose}
      aria-labelledby="alert-dialog-title"
      aria-describedby="alert-dialog-description"
    >
      <DialogTitle id="alert-dialog-title">
        {"Error !"}
      </DialogTitle>
      <DialogContent>
        <DialogContentText id="alert-dialog-description">
        The video file {filenamekun}is not exist.
        </DialogContentText>
      </DialogContent>
      <DialogActions>
        <Button onClick={handleClose} autoFocus>
          OK
        </Button>
      </DialogActions>
    </Dialog>
  </div>
    );
  }
  return (
    <>
      <h1>Hello Work!</h1>
      <br />
      {DialogAlertkun(filenotfoundialogopen,handlefilenotfoundialogclose,vfilename)}
      <Box sx={{ width: '100%' }}>
        <Stepper activeStep={activeStep}>
          {steps.map((label, index) => {
            const stepProps: { completed?: boolean } = {};
            const labelProps: {
              optional?: React.ReactNode;
            } = {};
            if (isStepOptional(index)) {
              labelProps.optional = (
                <Typography variant="caption">Optional</Typography>
              );
            }
            if (isStepSkipped(index)) {
              stepProps.completed = false;
            }
            return (
              <Step key={label} {...stepProps}>
                <StepLabel {...labelProps}>{label}</StepLabel>
              </Step>
            );
          })}
        </Stepper>
        {activeStep === steps.length ? (
          <React.Fragment>
            <Typography sx={{ mt: 2, mb: 1 }}>
              All steps completed - you&apos;re finished
            </Typography>
            <Box sx={{ display: 'flex', flexDirection: 'row', pt: 2 }}>
              <Box sx={{ flex: '1 1 auto' }} />
              <Button onClick={handleReset}>Reset</Button>
            </Box>
          </React.Fragment>
        ) : (
          <React.Fragment>
            {
              naibuyouso()
            }
            <Box sx={{ display: 'flex', flexDirection: 'row', pt: 2 }}>
              <Button
                color="inherit"
                disabled={activeStep === 0}
                onClick={handleBack}
                sx={{ mr: 1 }}
              >
                Back
              </Button>
              <Box sx={{ flex: '1 1 auto' }} />
              <Button onClick={handleNext}>
                {activeStep === steps.length - 1 ? 'Finish' : 'Next'}
              </Button>
            </Box>
          </React.Fragment>
        )}
      </Box>
      <br />
    </>
  )
}