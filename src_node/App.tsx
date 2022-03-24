import * as React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import IndexPage from './pages/IndexPage';
class App extends React.Component{
    public render():React.ReactNode{
        return(
            <>
            <BrowserRouter>
                <Routes>
                    <Route path="/" element={<IndexPage />}/>
                    <Route path="/index.html" element={<IndexPage />}/>
                </Routes>
            </BrowserRouter>
            </>
        );
    }
}
export default App;