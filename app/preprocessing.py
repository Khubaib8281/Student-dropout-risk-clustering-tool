def clean_engineer_features(df):

    df = df.copy()
    df.fillna(0, inplace = True)

    df['avg_quiz_score'] = df[['quiz1_marks', 'quiz2_marks', 'quiz3_marks']].mean(axis=1)
    df['assignment_completion_ratio'] = df['assignments_submitted'] / df['total_assignments']
    df['attendance_percentage'] = (df['lectures_attended'] / df['total_lectures'])*100
    df['lab_participation_ratio'] = df['labs_attended'] / df['total_lab_sessions'].replace(0, 1)
    df['exam_score_avg'] = (df['midterm_marks'] + df['final_marks']) / 2
    df['total_score'] = df[['quiz1_marks', 'quiz2_marks', 'quiz3_marks',
                            'midterm_marks', 'final_marks']].sum(axis=1)
    return df


def categorize_performance(score):
    if score < 50:
        return 'Low Achiever'
    elif 50 <= score < 75:
        return 'Average Achiever'
    else:
        return 'High Achiever'

def categorize_participation(attendance, assignment_ratio, lab_ratio=None):
    scores = [attendance, assignment_ratio * 100]
    if lab_ratio is not None:
        scores.append(lab_ratio * 100)

    participation_score = sum(scores) / len(scores)
    
    if participation_score < 40:
        return 'Low Participant'
    elif 40 <= participation_score < 70:
        return 'Average Participant'
    else:
        return 'High Participant'


    
def label_risk(df):
    """
    Assign risk labels to each student based on their cluster's behavior score.
    Supports exactly 5 clusters.
    """

    # Weighted behavior score (tune as needed)
    df['behavior_score'] = (
        0.4 * df['attendance_percentage'] +
        0.2 * (df['assignment_completion_ratio'] * 100) +
        0.2 * df['avg_quiz_score'] +
        0.1 * df['midterm_marks'] +
        0.1 * df['final_marks']
    )

    # Calculate mean behavior score per cluster
    cluster_scores = df.groupby('cluster')['behavior_score'].mean()

    # Rank clusters (lowest score = highest risk)
    sorted_clusters = cluster_scores.sort_values().index.tolist()

    # 5-level risk labels
    labels = ["High Risk", "Moderate Risk", "Mild Risk", "Low Risk", "No Risk"]
    cluster_to_label = {cluster: labels[i] for i, cluster in enumerate(sorted_clusters)}

    # Map risk label to each student
    df['risk_label'] = df['cluster'].map(cluster_to_label)

    # Optional cleanup
    df.drop(columns=['behavior_score'], inplace=True)

    return df

