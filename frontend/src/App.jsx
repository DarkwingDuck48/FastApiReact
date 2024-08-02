import { BrowserRouter, Routes, Route } from "react-router-dom";
import LoginForm from "./loginForm";
import Homepage from "./homepage";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<LoginForm />} />
        <Route path="/homepage" element={<Homepage />} />
      </Routes>
    </BrowserRouter>
  );
}
