import React, { useEffect, useState } from 'react';
import { View, Text, Button, TextInput, FlatList } from 'react-native';

const API = "http://10.0.2.2:8000"; // Android emulator: 10.0.2.2 or use local LAN IP

export default function App() {
  const [amount, setAmount] = useState("");
  const [category, setCategory] = useState("");
  const [pred, setPred] = useState(null);

  async function sendTx() {
    const res = await fetch(`${API}/transactions/`, {
      method: "POST",
      headers: {'Content-Type':'application/json'},
      body: JSON.stringify({ amount: parseFloat(amount), category })
    });
    const j = await res.json();
    alert("Tx saved id: " + j.id);
  }

  async function getPred() {
    const res = await fetch(`${API}/predict_next_month`, {
      method: "POST",
      headers: {'Content-Type':'application/json'},
      body: JSON.stringify({ user_id: 1 })
    });
    const j = await res.json();
    setPred(j.next_month_expense);
  }

  return (
    <View style={{ padding: 20, marginTop: 50 }}>
      <Text>Quick Expense Input</Text>
      <TextInput keyboardType="numeric" placeholder="Amount" value={amount} onChangeText={setAmount} style={{borderWidth:1, marginVertical:8}} />
      <TextInput placeholder="Category" value={category} onChangeText={setCategory} style={{borderWidth:1, marginBottom:8}} />
      <Button title="Save Transaction" onPress={sendTx} />
      <View style={{height:20}}/>
      <Button title="Predict Next Month Expense" onPress={getPred} />
      { pred && <Text style={{marginTop:20}}>Prediction: {pred}</Text> }
    </View>
  );
}
