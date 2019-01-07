const child=require("child_process");

command="dir";

child.exec(command,(error,stdout,stderr)=>{
	console.log(error);
	console.log(stdout);
	console.log(stderr);
});