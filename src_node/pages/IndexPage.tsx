import { Box, Button, Step, StepLabel, Stepper, Typography } from '@mui/material';
import React, * as react from 'react';

const steps = ['Select File Name', 'Create an ad group', 'Create an ad'];
export default function IndexPage(): React.ReactElement {
  const [vfilename, setvfilename] = React.useState<string>(null!);
  const [activeStep, setActiveStep] = React.useState(0);
  const [skipped, setSkipped] = React.useState(new Set<number>());

  const isStepOptional = (step: number) => {
    return step === 1;
  };

  const isStepSkipped = (step: number) => {
    return skipped.has(step);
  };

  const button_clicked = () => {
    //console.log("clicked");
    window.mia_electron_api.openVideoFileDialog("Open File").then(
      (pathobj) => {
        if (pathobj.status === true) {
          setvfilename(pathobj.path);
        } else {
          setvfilename("none");
        }
      });
  };
  const handleNext = () => {
    switch (activeStep) {
      case 0:
        console.log("Zero");
        window.mia_electron_api.fileExistsAsync(vfilename).then((result) => {
          if (result) {

            let newSkipped = skipped;
            if (isStepSkipped(activeStep)) {
              newSkipped = new Set(newSkipped.values());
              newSkipped.delete(activeStep);
            }

            setActiveStep((prevActiveStep) => prevActiveStep + 1);
            setSkipped(newSkipped);
          }else{
            console.log("You can't");
          }
        }
        );
        return;
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
  const naibuyouso = () => {
    switch (activeStep) {
      case 0:
        return (
          <>

            {vfilename}
            <br />
            <Button onClick={button_clicked}>
              Click me!
            </Button>
            <br />
          </>
        );
      case 1:
        return "One!";
      default:
        return "Default!";
    }
  }
  return (
    <>
      <h1>Hello Work!</h1>
      <br />
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