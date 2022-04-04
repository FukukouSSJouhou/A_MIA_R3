import * as React from 'react';
import { HashRouter, Route, Routes } from 'react-router-dom';
import ImageSelectPage from './pages/ImageSelectPage';
import IndexPage from './pages/IndexPage';
class App extends React.Component{
    public render():React.ReactNode{
        return(
            <>
            <HashRouter>
                <Routes>
                    <Route path="/" element={<IndexPage />}/>
                    <Route path="/index.html" element={<IndexPage />}/>
                </Routes>
            </HashRouter>
            </>
        );
    }
}
export default App;