import { StatusBar } from 'expo-status-bar';
import React, {useState} from 'react';
import { StyleSheet, Text, View, Button, TextInput } from 'react-native';

export default function App() {

  const[name, setName] = useState('Gustavo')

  const handleClick = () => {
    if (name == 'Gustavo'){
      setName('Manuel1')
    }
    else{
      setName('Gustavo')
    }
  }
  return (
    <View style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.headerText}>This is just a sample text</Text>
        <StatusBar style="auto" />
      </View>
      <View style={styles.body}>
        <Text style={styles.testText}>Babinga</Text>
        <Text style={styles.testText}>My name is {name}</Text>

        <View style={styles.buttonContainer}>
          <Button title='Press me to change name.' onPress={handleClick}/> 

        </View>
        <StatusBar style="auto" />
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#99ffff',
    alignItems: 'center',
    justifyContent: 'center',
  },

  body: {
    flex: 1,
    backgroundColor: '#ff0fff',
    alignItems: 'center',
    justifyContent: 'center',
  },


  header: {
    padding: 20,
    backgroundColor: '#00ffff',
  },

  testText: {
    fontSize: 30,
    color: '#ffffff',
  },
});
