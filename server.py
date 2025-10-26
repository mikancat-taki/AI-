# server.py
from flask import Flask, render_template, request, jsonify
from ai.markov import MarkovAI
from ai.memory import Memory
# optionally import other models when ready
# from ai.npnn import SimpleCharNN
# from ai.transformer import T
