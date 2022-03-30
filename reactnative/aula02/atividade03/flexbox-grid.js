import React from "react";
import { StyleSheet, View, Text } from "react-native";

const Square = ({ text }) => (
  <View style={styles.square}>
    <Text style={styles.text}>{text}</Text>
  </View>
);

export default function App() {
  return (
    <View style={styles.container}>
      <View style={styles.row}>
        <Square text="A" />
        <Square text="B" />
        <Square text="C" />
      </View>
      <View style={styles.row}>
        <Square text="D" />
        <Square text="E" />
        <Square text="F" />
      </View>
      <View style={styles.row}>
        <Square text="G" />
        <Square text="H" />
        <Square text="I" />
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
    container: {
      flex: 1,
      backgroundColor: "#7CA1B4",
      alignItems: "center",
      justifyContent: "center",
    },
    row: {
      flexDirection: "row",
    },
    square: {
        borderColor: "#fff",
        borderWidth: 1,
        width: 100,
        height: 100,
        justifyContent: "center",
        alignItems: "center",
      },
    text: {
    color: "#fff",
    fontSize: 18,
    fontWeight: "bold",
    }
  });