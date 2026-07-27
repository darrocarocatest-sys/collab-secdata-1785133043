const cp=require("child_process");
module.exports=function(req,res){ const n=req.query.name; cp.exec("echo "+n, (e,o)=>res.end(o)); };
