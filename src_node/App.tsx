import * as React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import ImageSelectPage from './pages/ImageSelectPage';
import IndexPage from './pages/IndexPage';
class App extends React.Component{
    public render():React.ReactNode{
        return(
            <>
            <BrowserRouter>
                <Routes>
                    <Route path="/" element={<ImageSelectPage />}/>
                    <Route path="/index.html" element={<IndexPage />}/>
                </Routes>
            </BrowserRouter>
            </>
        );
    }
}
export default App;