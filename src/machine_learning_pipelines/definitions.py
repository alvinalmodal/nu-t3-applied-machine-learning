import dagster as dg

from machine_learning_pipelines.assets.sentiment_analysis import sentiment_data, data_transformation, \
    tfidf_model_training, \
    evaluate_tfidf_sentiment_data, decision_tree_model_training, evaluate_decision_tree_sentiment_data

defs = dg.Definitions(
    assets=[sentiment_data, data_transformation, tfidf_model_training, evaluate_tfidf_sentiment_data,
            decision_tree_model_training, evaluate_decision_tree_sentiment_data],
    resources={},
)
