import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';

export default function App() {
  return (
    <View style={styles.container}>
      <StatusBar hidden={true} />
      <View style={styles.box1}></View>
      <View style={styles.box2}></View>
      <View style={styles.box3}></View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    // flexDirection: 'row',
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  box1: {
    backgroundColor: '#F5C371',
    width: 100,
    height: 100,
    // alignSelf: 'flex-start'
  },
  box2: {
    backgroundColor: '#BE706E',
    width: 100,
    height: 100,
    margin: 10,
  },
  box3: {
    backgroundColor: '#73495F',
    width: 100,
    height: 100,
    // alignSelf: 'flex-end'
  }
});
