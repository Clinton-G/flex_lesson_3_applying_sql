import mysql.connector
from mysql.connector import Error

db_name = 'Lesson_2_Assignment_Structured_Query_Language'
user = 'root'
password = 'password'  # Not My Real Password
host = 'localhost'


def add_member(id, name, age):
    try:
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )

        if conn.is_connected():
            cursor = conn.cursor()

            insert_query = """
            INSERT INTO Members (id, name, age)
            VALUES (%s, %s, %s)
            """

            member_data = (id, name, age)

            cursor.execute(insert_query, member_data)

            conn.commit()

            print('Member', name, 'Added Successfully with ID:', id)

    except Error as e:
        print(f"Error: {e}")
        print('Failed to Add', name)

    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()
            print('MySQL Connection Now Closed')


def add_workout_session(member_id, date, duration_minutes, calories_burned):

    try:
        conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host
        )

        if conn.is_connected():
            cursor = conn.cursor()

            insert_query = """
            INSERT INTO WorkoutSessions (member_id, session_date, duration_minutes, calories_burned)
            VALUES (%s, %s, %s, %s)
            """

            session_data = (member_id, date, duration_minutes, calories_burned)

            cursor.execute(insert_query, session_data)

            conn.commit()

            print('Workout Session Added Successfully for', member_id)

    except Error as e:
        print(f"Error: {e}")
        print('Failed to Add Workout for', member_id)

    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()
            print('MySQL Connection Now Closed')


def update_member_age(member_id, new_age):
    try:
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )

        if conn.is_connected():
            cursor = conn.cursor()

            check_query = "SELECT COUNT(*) FROM Members WHERE id = %s"
            cursor.execute(check_query, (member_id,))
            count = cursor.fetchone()[0]

            if count == 0:
                print(member_id, 'Not Found')
                return

            update_query = "UPDATE Members SET age = %s WHERE id = %s"
            cursor.execute(update_query, (new_age, member_id))

            conn.commit()

            print('Member', member_id, 'Updated Successfully to', new_age)

    except Error as e:
        print(f"Error: {e}")
        print('Failed to Update Age for', member_id)

    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()
            print('MySQL Connection Now Closed')


def delete_workout_session(session_id):
    try:
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )

        if conn.is_connected():
            cursor = conn.cursor()

            check_query = "SELECT COUNT(*) FROM WorkoutSessions WHERE session_id = %s"
            cursor.execute(check_query, (session_id,))
            count = cursor.fetchone()[0]

            if count == 0:
                print('Workout Session', session_id, 'Not Found')
                return

            delete_query = "DELETE FROM WorkoutSessions WHERE session_id = %s"
            cursor.execute(delete_query, (session_id,))

            conn.commit()

            print('Workout Session', session_id, 'Deleted Successfully')

    except Error as e:
        print(f"Error: {e}")
        print('Failed to Delete Workout')

    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()
            print('MySQL Connection Now Closed')


def get_members_in_age_range(start_age, end_age):
    try:
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )

        if conn.is_connected():
            cursor = conn.cursor(dictionary=True)

            query = """
            SELECT * FROM Members
            WHERE age BETWEEN %s AND %s
            """
            cursor.execute(query, (start_age, end_age))

            results = cursor.fetchall()

            if results:
                for row in results:
                    print(row['id'], row['name'], row['age'])
            else:
                print('No Members Found for Ages', start_age, 'and', end_age)

    except Error as e:
        print(f"Error: {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()
            print('MySQL Connection Now Closed')


if __name__ == "__main__":
    get_members_in_age_range(25, 30)
