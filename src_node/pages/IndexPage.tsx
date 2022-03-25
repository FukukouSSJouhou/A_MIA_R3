import { Button } from '@mui/material';
import React, * as react from 'react';
export default function IndexPage():React.ReactElement{
    const [vfilename,setvfilename]=React.useState<string>(null!);
    const button_clicked=()=>{
        //console.log("clicked");
        window.mia_electron_api.openVideoFileDialog("Open File").then(
            (pathobj)=>{
                if(pathobj.status===true){
                    setvfilename(pathobj.path);
                }else{
                    setvfilename("none");
                }
            });
    };
    return(
        <>
        <h1>Hello Work!</h1>
        <br/>
        {vfilename}
        <br />
        <Button onClick={button_clicked}>
            Click me!
        </Button>
        </>
    )
}