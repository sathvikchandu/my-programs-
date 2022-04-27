import logo from './logo.svg';
import './App.css';
import './blogcard'
import BlogCard from './blogcard';

function App() {
  const namef="Sathvik"

  const lname="chandu"
  const age=20

  const getfullname=()=>{
    return `${namef} ${lname}`
  }

  const styles={
    margin:"16px",
    boxShadow:"0px 2px 5px #ccc",
    borderRadius:"10px",
    padding:"16px",
    boxSizing:"border-box",
    color:"red", 
  }


  const arr=[{
    id:1,
    name:"sathvik",
   
    description:"hello this is sathvik"
  },
  {
    id:2,
    name:"unknown",
    
    description:"hello this is unknown"
  }]
  const blogcard=arr.map((item,pos)=>{
    
    console.log(item)
    return(

      <BlogCard key={pos} title="Test titles" name="kira"/>
     // <div style={styles} key={item.id}>
       // <h1>{item.name}</h1>
       // <p>{item.description}</p>
      //</div>
    )
  })

  
  
  return (
    
    <div className="App">
      {blogcard}
      <div style={
        {
          margin:"16px",
          boxShadow:"0px 2px 5px #ccc",
          borderRadius:"10px",
          padding:"16px",
          boxSizing:"border-box",
        }

      }>
        <h1>Welcome to the world of madness! {`${namef } ${lname}`}</h1>
        <h1>Welcome to the world of madness! {getfullname()}</h1>
        <input placeholder="Enter some random text yo! " />
      </div>
      <hr></hr>
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>

        

        <div style={styles}>
        <h1>Bye bye! {`${namef } ${lname}`}</h1>
        <h1>see you again! {getfullname()}</h1>
        </div>
      </header>
    </div>
  );
}

export default App;
