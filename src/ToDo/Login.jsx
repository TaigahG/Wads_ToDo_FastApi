import React, { useState, useEffect } from "react";
import { useNavigate, Link } from "react-router-dom";
import { getAuth, signInWithEmailAndPassword, onAuthStateChanged, GoogleAuthProvider, signInWithPopup } from "firebase/auth";
import "./Login.css";
const Login = () => {
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [loginError, setLoginError] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      await signInWithEmailAndPassword(getAuth(), email, password);
      navigate("/ToDo");
    } catch (error) {
      setLoginError("Invalid email or password, please try again.");
    }
  };

  const handleGoogleSignIn = async () => {
    const provider = new GoogleAuthProvider();
    try {
      await signInWithPopup(getAuth(), provider);
      navigate("/ToDo");
    } catch (error) {
      console.error("Google sign-in error:", error);
      setLoginError("Failed to sign in with Google. Please try again.");
    }
  };

  useEffect(() => {
    const unsubscribe = onAuthStateChanged(getAuth(), (user) => {
      if (user) {
        navigate("/");
      }
    });
    return () => unsubscribe();
  }, [navigate]);

  return (
    <div className="login">
      <div className="login__container">
        <h1>Sign In</h1>
        {loginError && <p className="login__error">{loginError}</p>}
        <form onSubmit={handleLogin}>
          <input type="email" className="login__textBox" placeholder="Email Address" value={email} onChange={(e) => setEmail(e.target.value)} required />
          <input type="password" className="login__textBox" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} required />
          <button type="submit" className="login__btn">
            Sign in
          </button>
        </form>
        <button onClick={handleGoogleSignIn} className="login__btn login__google">
          Sign in with Google
        </button>
        <p>
          Don't have an account?{" "}
          <Link to="/register" className="login__link">
            Sign up
          </Link>
        </p>
      </div>
    </div>
  );
};

export default Login;
