import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Image } from 'react-native';

export default function App() {
  return (
    <View style={styles.container}>
      <StatusBar hidden={true} />
      <Image
        source={require('./src/image/avatar.png')}
      />
      <Text style={styles.name}>Rafael M Puyau</Text>
      <Text>Data Scientist | Data Engineer | Python | Flask </Text>
      <Text style={styles.email}>rafael.puyau@gmail.com</Text>
      <View style={styles.contato}>
        <Image 
          source={require('./src/image/whatsapp.png')}
          style={{width: 35, height: 35}}
        />
        <Text style={styles.tel}>24 99262.1265</Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  name: {
    fontSize: 24,
    margin: 20
  },
  email: {
    marginTop: 10,
    marginBottom: 10
  },
  contato: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  tel: {
    // fontSize: 25,
    marginLeft: 10
  }
});
