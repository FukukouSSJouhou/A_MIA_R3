let WSServer=require("ws").Server;
let ws=new WSServer({port:5001});
let connections = [];
function broadcast(message) {
    connections.forEach((con, i)=> {
        con.send(message);
    });
};
ws.on("connection",(ws)=>{
    connections.push(ws);
    ws.on("close",()=>{
        connections=connections.filter((conn,i)=>{
            return (conn===ws)?false:true;
        });
    });
    ws.on("message",(message)=>{
        let objtdn=JSON.parse(message);
        switch(objtdn.command){
            case "test":

                let objkun={
                    "command":"selectimg",
                    "data":[
                        "https://via.placeholder.com/300x300",
                        "https://via.placeholder.com/300x300",
                        "https://via.placeholder.com/300x300",
                        "https://via.placeholder.com/300x300",
                        "https://via.placeholder.com/300x300"
                    ]
                }
                broadcast(JSON.stringify(objkun));
                break;
        }
        console.log("recieved: %s",JSON.stringify(objtdn))  
    })
});
