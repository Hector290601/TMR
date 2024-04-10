// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from drive_base_msgs:msg/BaseInfo.idl
// generated code does not contain a copyright notice

#include "drive_base_msgs/msg/detail/base_info__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_drive_base_msgs
const rosidl_type_hash_t *
drive_base_msgs__msg__BaseInfo__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x2b, 0xf1, 0xb6, 0xde, 0xd5, 0x03, 0x67, 0x0d,
      0x45, 0xde, 0xf4, 0x72, 0x98, 0x79, 0x6d, 0xe2,
      0xbd, 0x05, 0xff, 0x6b, 0x3e, 0x06, 0xe9, 0x76,
      0x84, 0xe9, 0x89, 0xd8, 0x22, 0x94, 0xdb, 0x7c,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types
#include "builtin_interfaces/msg/detail/time__functions.h"

// Hashes for external referenced types
#ifndef NDEBUG
static const rosidl_type_hash_t builtin_interfaces__msg__Time__EXPECTED_HASH = {1, {
    0xb1, 0x06, 0x23, 0x5e, 0x25, 0xa4, 0xc5, 0xed,
    0x35, 0x09, 0x8a, 0xa0, 0xa6, 0x1a, 0x3e, 0xe9,
    0xc9, 0xb1, 0x8d, 0x19, 0x7f, 0x39, 0x8b, 0x0e,
    0x42, 0x06, 0xce, 0xa9, 0xac, 0xf9, 0xc1, 0x97,
  }};
#endif

static char drive_base_msgs__msg__BaseInfo__TYPE_NAME[] = "drive_base_msgs/msg/BaseInfo";
static char builtin_interfaces__msg__Time__TYPE_NAME[] = "builtin_interfaces/msg/Time";

// Define type names, field names, and default values
static char drive_base_msgs__msg__BaseInfo__FIELD_NAME__hw_id[] = "hw_id";
static char drive_base_msgs__msg__BaseInfo__FIELD_NAME__hw_timestamp[] = "hw_timestamp";
static char drive_base_msgs__msg__BaseInfo__FIELD_NAME__stamp[] = "stamp";
static char drive_base_msgs__msg__BaseInfo__FIELD_NAME__x[] = "x";
static char drive_base_msgs__msg__BaseInfo__FIELD_NAME__y[] = "y";
static char drive_base_msgs__msg__BaseInfo__FIELD_NAME__orientation[] = "orientation";
static char drive_base_msgs__msg__BaseInfo__FIELD_NAME__forward_velocity[] = "forward_velocity";
static char drive_base_msgs__msg__BaseInfo__FIELD_NAME__rotational_velocity[] = "rotational_velocity";
static char drive_base_msgs__msg__BaseInfo__FIELD_NAME__battery_voltage_pct[] = "battery_voltage_pct";
static char drive_base_msgs__msg__BaseInfo__FIELD_NAME__power_supply[] = "power_supply";
static char drive_base_msgs__msg__BaseInfo__FIELD_NAME__overcurrent[] = "overcurrent";
static char drive_base_msgs__msg__BaseInfo__FIELD_NAME__blocked[] = "blocked";
static char drive_base_msgs__msg__BaseInfo__FIELD_NAME__in_collision[] = "in_collision";
static char drive_base_msgs__msg__BaseInfo__FIELD_NAME__at_cliff[] = "at_cliff";
static char drive_base_msgs__msg__BaseInfo__FIELD_NAME__safety_state[] = "safety_state";

static rosidl_runtime_c__type_description__Field drive_base_msgs__msg__BaseInfo__FIELDS[] = {
  {
    {drive_base_msgs__msg__BaseInfo__FIELD_NAME__hw_id, 5, 5},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_UINT32,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {drive_base_msgs__msg__BaseInfo__FIELD_NAME__hw_timestamp, 12, 12},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_UINT32,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {drive_base_msgs__msg__BaseInfo__FIELD_NAME__stamp, 5, 5},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {builtin_interfaces__msg__Time__TYPE_NAME, 27, 27},
    },
    {NULL, 0, 0},
  },
  {
    {drive_base_msgs__msg__BaseInfo__FIELD_NAME__x, 1, 1},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {drive_base_msgs__msg__BaseInfo__FIELD_NAME__y, 1, 1},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {drive_base_msgs__msg__BaseInfo__FIELD_NAME__orientation, 11, 11},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {drive_base_msgs__msg__BaseInfo__FIELD_NAME__forward_velocity, 16, 16},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {drive_base_msgs__msg__BaseInfo__FIELD_NAME__rotational_velocity, 19, 19},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {drive_base_msgs__msg__BaseInfo__FIELD_NAME__battery_voltage_pct, 19, 19},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_UINT8,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {drive_base_msgs__msg__BaseInfo__FIELD_NAME__power_supply, 12, 12},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_UINT8,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {drive_base_msgs__msg__BaseInfo__FIELD_NAME__overcurrent, 11, 11},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_BOOLEAN,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {drive_base_msgs__msg__BaseInfo__FIELD_NAME__blocked, 7, 7},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_BOOLEAN,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {drive_base_msgs__msg__BaseInfo__FIELD_NAME__in_collision, 12, 12},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_BOOLEAN,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {drive_base_msgs__msg__BaseInfo__FIELD_NAME__at_cliff, 8, 8},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_BOOLEAN,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {drive_base_msgs__msg__BaseInfo__FIELD_NAME__safety_state, 12, 12},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_UINT16,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

static rosidl_runtime_c__type_description__IndividualTypeDescription drive_base_msgs__msg__BaseInfo__REFERENCED_TYPE_DESCRIPTIONS[] = {
  {
    {builtin_interfaces__msg__Time__TYPE_NAME, 27, 27},
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
drive_base_msgs__msg__BaseInfo__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {drive_base_msgs__msg__BaseInfo__TYPE_NAME, 28, 28},
      {drive_base_msgs__msg__BaseInfo__FIELDS, 15, 15},
    },
    {drive_base_msgs__msg__BaseInfo__REFERENCED_TYPE_DESCRIPTIONS, 1, 1},
  };
  if (!constructed) {
    assert(0 == memcmp(&builtin_interfaces__msg__Time__EXPECTED_HASH, builtin_interfaces__msg__Time__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[0].fields = builtin_interfaces__msg__Time__get_type_description(NULL)->type_description.fields;
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "uint8 POWER_SUPPLY_STATUS_UNKNOWN = 0\n"
  "uint8 POWER_SUPPLY_STATUS_CHARGING = 1\n"
  "uint8 POWER_SUPPLY_STATUS_DISCHARGING = 2\n"
  "uint8 POWER_SUPPLY_STATUS_NOT_CHARGING = 3\n"
  "uint8 POWER_SUPPLY_STATUS_FULL = 4\n"
  "\n"
  "# OR'able bits to communicate current safety state as determined by base sensors\n"
  "uint16 SAFETY_STATE_OPERATIONAL = 1\n"
  "uint16 SAFETY_STATE_LOW_SPEED   = 2\n"
  "uint16 SAFETY_STATE_NO_FORWARD  = 4\n"
  "uint16 SAFETY_STATE_NO_BACKWARD = 8\n"
  "uint16 SAFETY_STATE_NO_ROTATE   = 16\n"
  "\n"
  "# identifying information\n"
  "uint32 hw_id                  # a, hopefully unique, id\n"
  "uint32 hw_timestamp           # timestamp as returned by the hardware\n"
  "builtin_interfaces/Time stamp # wall clock timestamp\n"
  "\n"
  "# position information (estimated, relative to starting pose)\n"
  "float32 x\n"
  "float32 y\n"
  "float32 orientation\n"
  "# should we add z?\n"
  "\n"
  "# velocity information\n"
  "float32 forward_velocity\n"
  "float32 rotational_velocity\n"
  "\n"
  "# battery state\n"
  "uint8 battery_voltage_pct     # range: 0-100. current battery voltage as percent of nominal.\n"
  "uint8 power_supply            # one of the constants above\n"
  "\n"
  "# diagnostic information\n"
  "bool overcurrent              # motor overcurrent detected\n"
  "bool blocked                  # True if forward direction is blocked by an obstacle\n"
  "bool in_collision             # True if the robot is in collision (usually detected via bumper)\n"
  "bool at_cliff                 # True if the robot has detected a cliff in the forward direction\n"
  "\n"
  "uint16 safety_state";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
drive_base_msgs__msg__BaseInfo__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {drive_base_msgs__msg__BaseInfo__TYPE_NAME, 28, 28},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 1415, 1415},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
drive_base_msgs__msg__BaseInfo__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[2];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 2, 2};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *drive_base_msgs__msg__BaseInfo__get_individual_type_description_source(NULL),
    sources[1] = *builtin_interfaces__msg__Time__get_individual_type_description_source(NULL);
    constructed = true;
  }
  return &source_sequence;
}
