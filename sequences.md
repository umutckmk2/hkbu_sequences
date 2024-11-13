-- SEQUENCE: public.locations_id_seq

-- DROP SEQUENCE IF EXISTS public.locations_id_seq;

CREATE SEQUENCE IF NOT EXISTS public.locations_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;

ALTER SEQUENCE public.locations_id_seq
    OWNER TO "kiffin.tse";





-- SEQUENCE: public.registers_id_seq

-- DROP SEQUENCE IF EXISTS public.registers_id_seq;

CREATE SEQUENCE IF NOT EXISTS public.registers_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;

ALTER SEQUENCE public.registers_id_seq
    OWNER TO "kiffin.tse";





-- SEQUENCE: public.can_labtest_uploads_id_seq

-- DROP SEQUENCE IF EXISTS public.can_labtest_uploads_id_seq;

CREATE SEQUENCE IF NOT EXISTS public.can_labtest_uploads_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;

ALTER SEQUENCE public.can_labtest_uploads_id_seq
    OWNER TO "kiffin.tse";



-- SEQUENCE: public.action_tip_translations_id_seq

-- DROP SEQUENCE IF EXISTS public.action_tip_translations_id_seq;

CREATE SEQUENCE IF NOT EXISTS public.action_tip_translations_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;

ALTER SEQUENCE public.action_tip_translations_id_seq
    OWNED BY public.action_tip_translations.id;

ALTER SEQUENCE public.action_tip_translations_id_seq
    OWNER TO "kiffin.tse";




-- SEQUENCE: public.action_tips_id_seq

-- DROP SEQUENCE IF EXISTS public.action_tips_id_seq;

CREATE SEQUENCE IF NOT EXISTS public.action_tips_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;

ALTER SEQUENCE public.action_tips_id_seq
    OWNED BY public.action_tips.id;

ALTER SEQUENCE public.action_tips_id_seq
    OWNER TO "kiffin.tse";



-- SEQUENCE: public.airflow_parameters_id_seq

-- DROP SEQUENCE IF EXISTS public.airflow_parameters_id_seq;

CREATE SEQUENCE IF NOT EXISTS public.airflow_parameters_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;

ALTER SEQUENCE public.airflow_parameters_id_seq
    OWNED BY public.airflow_parameters.id;

ALTER SEQUENCE public.airflow_parameters_id_seq
    OWNER TO "kiffin.tse";




-- SEQUENCE: public.appliance_categories_id_seq

-- DROP SEQUENCE IF EXISTS public.appliance_categories_id_seq;

CREATE SEQUENCE IF NOT EXISTS public.appliance_categories_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;

ALTER SEQUENCE public.appliance_categories_id_seq
    OWNED BY public.appliance_categories.id;

ALTER SEQUENCE public.appliance_categories_id_seq
    OWNER TO "kiffin.tse";



-- SEQUENCE: public.journals_attachments_id_seq

-- DROP SEQUENCE IF EXISTS public.journals_attachments_id_seq;

CREATE SEQUENCE IF NOT EXISTS public.journals_attachments_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.journals_attachments_id_seq
    OWNER TO "kiffin.tse";



-- SEQUENCE: public.journals_id_seq

-- DROP SEQUENCE IF EXISTS public.journals_id_seq;

CREATE SEQUENCE IF NOT EXISTS public.journals_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.journals_id_seq
    OWNER TO "kiffin.tse";


-- SEQUENCE: public.location_groups_id_seq

-- DROP SEQUENCE IF EXISTS public.location_groups_id_seq;

CREATE SEQUENCE IF NOT EXISTS public.location_groups_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;

ALTER SEQUENCE public.location_groups_id_seq
    OWNER TO "kiffin.tse";



-- SEQUENCE: public.monitorings_id_seq

-- DROP SEQUENCE IF EXISTS public.monitorings_id_seq;

CREATE SEQUENCE IF NOT EXISTS public.monitorings_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;

ALTER SEQUENCE public.monitorings_id_seq
    OWNER TO "kiffin.tse";


-- SEQUENCE: public.notification_attachments_id_seq

-- DROP SEQUENCE IF EXISTS public.notification_attachments_id_seq;

CREATE SEQUENCE IF NOT EXISTS public.notification_attachments_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.notification_attachments_id_seq
    OWNER TO "kiffin.tse";



-- SEQUENCE: public.rule2s_id_seq

-- DROP SEQUENCE IF EXISTS public.rule2s_id_seq;

CREATE SEQUENCE IF NOT EXISTS public.rule2s_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;

ALTER SEQUENCE public.rule2s_id_seq
    OWNER TO "kiffin.tse";



-- SEQUENCE: public.surveys_id_seq

-- DROP SEQUENCE IF EXISTS public.surveys_id_seq;

CREATE SEQUENCE IF NOT EXISTS public.surveys_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.surveys_id_seq
    OWNER TO "kiffin.tse";




-- SEQUENCE: public.user_notifications_id_seq

-- DROP SEQUENCE IF EXISTS public.user_notifications_id_seq;

CREATE SEQUENCE IF NOT EXISTS public.user_notifications_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.user_notifications_id_seq
    OWNER TO "kiffin.tse";

-- SEQUENCE: public.notifications_id_seq

-- DROP SEQUENCE IF EXISTS public.notifications_id_seq;

CREATE SEQUENCE IF NOT EXISTS public.notifications_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.notifications_id_seq
    OWNER TO "kiffin.tse";


-- SEQUENCE: public.user_preferences_id_seq

-- DROP SEQUENCE IF EXISTS public.user_preferences_id_seq;

CREATE SEQUENCE IF NOT EXISTS public.user_preferences_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;

ALTER SEQUENCE public.user_preferences_id_seq
    OWNER TO "kiffin.tse";





-- SEQUENCE: public.user_settings_id_seq

-- DROP SEQUENCE IF EXISTS public.user_settings_id_seq;

CREATE SEQUENCE IF NOT EXISTS public.user_settings_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;

ALTER SEQUENCE public.user_settings_id_seq
    OWNER TO postgres;




-- SEQUENCE: public.user_surveys_id_seq

-- DROP SEQUENCE IF EXISTS public.user_surveys_id_seq;

CREATE SEQUENCE IF NOT EXISTS public.user_surveys_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.user_surveys_id_seq
    OWNER TO "kiffin.tse";




-- SEQUENCE: public.users_id_seq

-- DROP SEQUENCE IF EXISTS public.users_id_seq;

CREATE SEQUENCE IF NOT EXISTS public.users_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;

ALTER SEQUENCE public.users_id_seq
    OWNER TO "kiffin.tse";




appliance categories

cities