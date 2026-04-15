function App() {
  return (
    <div>
      <h1 aria-hidden="true">
      Hidden Title
    </h1>
      <div onClick={() => alert("Hi")}>Click me</div>
      <input type="text" />
       <div tabIndex="0">
      Focus me
    </div>
    </div>
    
  );
}

export default App;