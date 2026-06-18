# Architecture du pipeline

Le pipeline est composé de plusieurs couches.

## 1. Collecte

Les données sont collectées depuis des sources de news comme Le Monde, AFP, Gorafi et Fact Check AFP.

## 2. Ingestion

Kafka est utilisé pour recevoir les news en temps réel sous forme de messages.

## 3. Traitement

Spark Streaming lit les messages Kafka, nettoie les données, extrait les champs nécessaires et applique une vérification automatique.

## 4. Stockage

Hadoop HDFS conserve l’historique complet des données collectées.

MongoDB stocke les informations traitées et exploitables.

## 5. Retraitement

Toutes les données historiques stockées dans HDFS peuvent être retraitées toutes les 6 heures.

## 6. Supervision

Des logs et indicateurs permettent de surveiller l’état du pipeline.