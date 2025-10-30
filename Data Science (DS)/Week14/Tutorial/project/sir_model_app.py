import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Streamlit UI
st.title("🦠 Stochastic SIR Model: Disease Spread Simulation")

# Sidebar inputs for parameters
st.sidebar.header("Simulation Parameters")

N = st.sidebar.slider("Total Population (N)", 500, 10_000, 1000, step=500)
I0 = st.sidebar.slider("Initial Infected (I₀)", 1, N//2, 1)
beta = st.sidebar.slider("Infection Rate (β)", 0.05, 1.0, 0.3, step=0.05)
gamma = st.sidebar.slider("Recovery Rate (γ)", 0.01, 0.5, 0.1, step=0.01)
days = st.sidebar.slider("Simulation Days", 10, 365, 100)

# Initialize compartments
S0 = N - I0
R0 = 0

# Store results
S, I, R = [S0], [I0], [R0]

# Run stochastic simulation
for day in range(days):
    new_infected = np.random.binomial(S[-1], beta * I[-1] / N) if S[-1] > 0 else 0
    new_recovered = np.random.binomial(I[-1], gamma) if I[-1] > 0 else 0

    S.append(S[-1] - new_infected)
    I.append(I[-1] + new_infected - new_recovered)
    R.append(R[-1] + new_recovered)

# Plot results
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(S, label="Susceptible", color="blue")
ax.plot(I, label="Infected", color="red")
ax.plot(R, label="Recovered", color="green")

ax.set_xlabel("Days")
ax.set_ylabel("Population")
ax.set_title("Stochastic SIR Model Simulation")
ax.legend()

st.pyplot(fig)