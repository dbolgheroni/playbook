#include <boost/type_index.hpp>
#define PBTYPE(x) boost::typeindex::type_id_with_cvr<decltype(x)>().pretty_name()

int pb(void);
